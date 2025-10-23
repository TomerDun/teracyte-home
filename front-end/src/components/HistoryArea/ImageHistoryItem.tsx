import imageIcon from '../../assets/icons/image-icon.svg';

interface ImageHistoryItemProps {
    imageId: string;
    createdAt: string;
}

export default function ImageHistoryItem({ imageId, createdAt }: ImageHistoryItemProps) {
    return (
        <div className="w-full bg-white border border-gray-200 rounded-lg p-4 flex items-center justify-between shadow-sm hover:shadow-md transition-all cursor-pointer">
            <div className="flex items-start gap-3">
                <img src={imageIcon} alt="" className="w-5 h-5 mt-0.5" />                
                    <p className="text-sm text-gray-500 leading-5">
                        {imageId}
                    </p>                
            </div>
            <div className="flex flex-col items-end">
                <p className="text-sm text-gray-500 leading-5">
                    {createdAt}
                </p>
            </div>
        </div>
    );
}