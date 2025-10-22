import defaultImage from '../../assets/images/ex-img.png';

// const defaultImage = "http://localhost:3845/assets/fdc0405d0a8d19a234a5265486668c2c565eece8.png";

interface ImageDisplayCardProps {
  imageUrl?: string;
  alt?: string;
}

export default function ImageDisplayCard({
  imageUrl = defaultImage,
  alt = "Display image"
}: ImageDisplayCardProps = {}) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl h-full w-full flex items-center justify-center p-6">
      <img 
        src={imageUrl} 
        alt={alt} 
        className="max-w-full max-h-full object-contain rounded"
      />
    </div>
  );
}