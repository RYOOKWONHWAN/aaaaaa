import React from "react";
import BarLoader from "react-spinners/BarLoader";

function Loading() {
    return (
        <div className="contentWrap">
            <div
                style={{
                    position: "fixed",
                    top: "50%",
                    left: "50%",
                    transform: "translate(-50%, -50%)",
                }}
            >
                <BarLoader
                    color="#C63DEE"
                    height={25}
                    width={400}

                />
            </div>
        </div>
    );
}

export default Loading;