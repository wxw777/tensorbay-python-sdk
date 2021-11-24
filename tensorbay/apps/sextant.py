#!/usr/bin/env python3
#
# Copyright 2021 Graviti. Licensed under MIT License.
#

"""Interact with sextant app at graviti marketplace."""

from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

from tensorbay.client.requests import Client


class Evaluation:
    """This class defines :class:`Evaluation`.

    Arguments:
        evaluation_id: Evaluation ID.
        benchmark: The :class:`Benchmark`.

    """

    def __init__(self, evaluation_id: str, benchmark: "Benchmark") -> None:
        self.evaluation_id = evaluation_id
        self.benchmark = benchmark

    def get_result(self) -> Dict[str, Any]:
        """Get the result of the evaluation.

        Return:
            The result dict of the evaluation.

        """

    def get_status(self) -> str:
        """Get the status of the evaluation.

        Return:
            One of "success", "fail" or "processing".

        """


class Benchmark:  # pylint: disable=too-many-instance-attributes
    """This class defines :class:`Benchmark`.

    Arguments:
        name: Name of the Benchmark.
        dataset_id: ID of the dataset on which this benchmark based.
        commit_id: ID of the commit which is used as the evaluation benchmark.
        benchmark_id: Benchmark ID.
        sextant: The :class:`SextantClient`.
        categories: The needed evaluation categories, if not given, all categories will be used.
        iou_threshold: The IoU threshold.
        customized_metrics: Https url of the github repository.

    """

    def __init__(
        self,
        name: str,
        benchmark_id: str,
        sextant: "Sextant",
        *,
        dataset_id: Optional[str] = None,
        commit_id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        iou_threshold: Optional[float] = None,
        customized_metrics: Optional[str] = None,
    ) -> None:
        self.name = name
        self.dataset_id = dataset_id
        self.benchmark_id = benchmark_id
        self.commit_id = commit_id
        self.sextant = sextant
        self.categories = categories
        self.iou_threshold = iou_threshold
        self.customized_metrics = customized_metrics

    def create_evaluation(self, dataset_id: str, commit_id: str) -> Evaluation:
        """Create an evaluation task.

        Arguments:
            dataset_id: Id of the needed evaluation dataset.
            commit_id: Id of the needed commit.

        Return:
            The created evaluation instance.

        """

    def list_evaluations(self) -> List[Evaluation]:
        """List all evaluations.

        Return:
            A list of evaluations.

        """


class Sextant(Client):
    """This class defines :class:`Sextant`.

    Arguments:
        access_key: User's access key.
        url: The URL of the graviti gas website.

    """

    def __init__(self, access_key: str, url: str = "") -> None:
        super().__init__(access_key, url)
        self._open_api = urljoin(self.gateway_url, "apps/sextant/")

    def create_benchmark(
        self,
        name: str,
        dataset_id: str,
        commit_id: str,
        *,
        categories: Optional[List[str]] = None,
        iou_threshold: Optional[float] = None,
        customized_metrics: Optional[str] = None,
    ) -> Benchmark:
        """Create a benchmark with the given parameters.

        Arguments:
            name: Name of the Benchmark.
            dataset_id: ID of the dataset on which this benchmark based.
            commit_id: ID of the commit which used as the evaluation benchmark.
            categories: The needed evaluation categories, if not given, all categories will be used.
            iou_threshold: The IoU threshold.
            customized_metrics: Https url of the github repository.

        Raises:# flake8: noqa: F402
            ValueError: When iou_threshold and customized_metrics both given or both not given.

        """

    def list_benchmarks(self) -> List[Benchmark]:
        """List all benchmarks.

        Return:
            The list of Benchmark instances.

        """

    def get_benchmark(self, name: str) -> Benchmark:
        """Get a benchmark instance by name.

        Arguments:
            name: Name of the Benchmark.

        Return:
            The Benchmark instance with the given name.

        """