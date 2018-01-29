package at.gmi.djamei.phenopipe;

import java.util.HashMap;

import java.util.UUID;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import io.reactivex.Observable;

//TODO Move to shared library
/**
 * Singleton to hold references to Observables which hold Progress responses generated by background tasks
 * @author Sebastian Seitner
 * 
 */
public enum JobMapper {
	INSTANCE;
	static final Logger logger = LogManager.getLogger();
	private final HashMap<UUID, Observable<ProgressResponse>> job2Observable=new HashMap<>();
	
	/**
	 * Add a Job which status observable will not complete on a specific message. Such jobs should be removed from the mapper manually
	 * @param jobID
	 * @param obs
	 */
	public void put(UUID jobID, Observable<ProgressResponse> obs){
		put(jobID,obs,null);
	}
	/**
	 * Adds a Jobs status Observable to the mapper which will be evicted when the status Observable emits a message that is equal to completeOn.
	 * Additionally the Observable which is stored will complete on the appearance of the String
	 * @param jobID
	 * @param obs
	 * @param completeOn
	 */
	public void put(UUID jobID, Observable<ProgressResponse> obs, String completeOn){
		obs= obs.takeWhile(resp->!resp.getMessage().equals(completeOn))
				.doOnTerminate(()->{this.remove(jobID);});
		
		job2Observable.put(jobID, obs);
		logger.debug("Added job {}", jobID);
	}
	public void remove(UUID jobID){
		job2Observable.remove(jobID);
		logger.debug("Removed job {}", jobID);
	}
	public Observable<ProgressResponse> get(UUID jobID){
		return job2Observable.get(jobID);
	}
}