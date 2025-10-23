import defaultImage from '../../assets/images/ex-img.png';
import { SERVER_BASE_URL } from '../../services/apiService';
import LoadingImage from '../misc/LoadingImage';

// const defaultImage = "http://localhost:3845/assets/fdc0405d0a8d19a234a5265486668c2c565eece8.png";

type ImageDisplayCardProps = {
  imageFilePath: string | null
}


export default function ImageDisplayCard({ imageFilePath }: ImageDisplayCardProps) {

  const fullImageUrl = SERVER_BASE_URL + imageFilePath;

  return (
    <div className="bg-white border border-gray-200 rounded-xl h-full w-full flex items-center justify-center p-6">
      {imageFilePath ?
        <img
          src={fullImageUrl}
          alt='cells-image'
          className="max-w-full max-h-full object-contain rounded"
        />
        :
        <div className='max-w-full max-h-full'>
          <LoadingImage />
        </div>
      }
    </div>
  );
}